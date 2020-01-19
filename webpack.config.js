const path = require('path');

module.exports = {
    entry: {
        gallery: './blog/static/src/js/components/masonry.js',
        modal: ['./blog/static/src/js/components/post_detail.js', './blog/static/src/js/components/confirm_delete.js'],
		form: ['./blog/static/src/js/components/upload_file.js', "./blog/static/src/js/components/manage_post.js"],
    },
    output: {
        path: path.join(`${__dirname}/blog/static/dist/`),
        filename: '[name].min.js'
    },
    watch: false,
    mode: 'production',
    devtool: "source-map",
    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
                "presets": [
                    ["env", {
                        "targets": {
                            "browsers": ["> 1%"]
                        }
                    }]
                ]
            }
        }],
    }
}