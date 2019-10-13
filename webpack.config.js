module.exports = {
    entry: './blog/static/src/js/app.js',
    output: {
        path: `${__dirname}/blog/static/dist/`,
        filename: 'bundle.min.js'
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