{
    'name': 'Anime Theme',
    'description': 'Anime theme for website',
    'category': 'Website/Theme',
    'version': '17.0',
    'author': 'Shashwati',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'data/presets.xml',
        'data/images.xml',
        'data/menu.xml',

        'views/website_templates.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/snippets/options.xml',
        'views/snippets/s_anime_hero.xml',
        'views/snippets/s_image_text.xml',

        'data/pages/categories.xml',
        'data/pages/login.xml'
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
            'website_comic/static/src/scss/categories.scss',
            'website_comic/static/src/snippets/s_anime_hero.scss',
            'website_comic/static/src/scss/login.scss',
        ]
    },
}