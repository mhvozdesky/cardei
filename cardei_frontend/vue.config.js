// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

// devServer: {
//   proxy: "http://localhost:8000"
// }

module.exports = {
  devServer: {
    proxy: {
      '^/api/v1': {
        // target: 'http://web:8000',
        target: 'http://localhost:8000',
        changeOrigin: true,
        logLevel: "debug",
      },
    }
  }
}
