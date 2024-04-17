{
    'name': 'Anime Theme',
    'description': 'Anime theme for website',
    'category': 'Website/Theme',
    'author': 'Shashwati',
    'license': 'LGPL-3',
    'depends': ['website','base'],
    'data': [
        'data/presets.xml',
        'data/images.xml',
        'data/menu.xml',

        'security/ir.model.access.csv',

        'views/anime_publisher.xml',
        'views/anime_author_views.xml',
        'views/anime_views.xml',
        'views/anime_menus.xml',

        'views/website_templates.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/snippets/options.xml',
        'views/snippets/s_anime_hero.xml',
        'views/snippets/s_banner.xml',

        'data/pages/categories.xml',
        'data/pages/login.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_comic/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            'website_comic/static/src/scss/bootstrap_overridden.scss',
        ],
        'web.assets_frontend': [
            'website_comic/static/src/scss/header.scss',
            'website_comic/static/src/scss/footer.scss',
            'website_comic/static/src/scss/fonts.scss',
            'website_comic/static/src/scss/categories.scss',
            'website_comic/static/src/snippets/s_banner.scss',
            'website_comic/static/src/snippets/s_anime_hero.scss',
            'website_comic/static/src/scss/login.scss',
            'website_comic/static/src/scss/responsive.scss',
        ]
    },
}