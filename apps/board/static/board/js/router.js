(function ($, Backbone, _, app) {
    var AppRouter = Backbone.Router.extend({
        routes: {
            '': 'home',
            'sprint/:id': 'sprint'
        },
        initialize: function (options) {
            this.contentElement = '#content';
            this.current = null;
            // Adding the header to make sure it is always present
            this.header = new app.views.HeaderView();
            $('body').prepend(this.header.el);
            this.header.render();
            Backbone.history.start();
        },
        home: function () {
            var view = new app.views.HomepageView({el: this.contentElement});
            this.render(view);
        },
        sprint: function (id) {
            var view = new app.views.SprintView({
                el: this.contentElement,
                sprintId: id
            });
            this.render(view);
        },
        route: function (route, name, callback) {
            // Override default route to enforce login on every page
            var login;
            callback = callback || this[name];
            // The original callback function will be wrapped to first check the authentication
            // state before calling
            callback = _.wrap(callback, function (original) {
                var args = _.without(arguments, original);
                if (app.session.authenticated()) {
                    // If the user is authenticated, the original callback is called
                    original.apply(this, args);
                } else {
                    // Show the login screen before calling the view
                    $(this.contentElement).hide();
                    // Bind the original callback once the login is successful
                    login = new app.views.LoginView();
                    $(this.contentElement).after(login.el);
                    login.on('done', function () {
                        // When the login is finished, the header is rendered again to reflect the new state (124).
                        this.header.render();
                        $(this.contentElement).show();
                        original.apply(this, args);
                    }, this);
                    // Render the login form
                    login.render();
                }
            });
            // The original route is called using the new wrapped callback
            return Backbone.Router.prototype.route.apply(this, [route, name, callback]);
        },
        render: function (view) {
            if (this.current) {
                this.current.undelegateEvents();
                this.current.$el = $();
                this.current.remove();
            }
            this.current = view;
            this.current.render();
        }
    });

    app.router = AppRouter;

})(jQuery, Backbone, _, app);