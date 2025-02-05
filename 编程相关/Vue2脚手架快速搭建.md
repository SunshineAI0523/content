---
title: Vue2脚手架快速搭建
icon: pen-to-square
date: 2024-09-12
category:
  - 编程学习
tag:
  - 编程学习
  - 前端技术
  - 自学编程
---
# 基于Vue.js和vue-router创建一个VUE2脚手架，我们可以分以下几个部分：

1. **项目初始化**
   首先确保你已经安装了Node.js。通过npm或yarn安装Vue CLI来创建一个新的Vue项目：

   ```bash
   npm install -g @vue/cli
   vue create myEnterpriseWebApp
   cd MyEnterpriseWebApp
   ```
2. **安装vue-router**
   添加vue-router到项目中：

   ```bash
   vue add router
   ```
3. **创建页面组件**
   在 `src/components`目录下创建以下组件（以首页和关于我们为例）：

   - `HomePage.vue`: 主页组件，包含欢迎语、标语等基本内容。
   - `AboutUsPage.vue`: 关于我们页面组件，展示企业的历史、团队信息以及企业愿景等。
4. **配置路由**
   在 `src/router/index.js`中配置Vue Router：

   ```javascript
   import Vue from 'vue'
   import Router from 'vue-router'
   import HomePage from '@/components/HomePage'
   import AboutUsPage from '@/components/AboutUsPage'

   Vue.use(Router)

   export default new Router({
     mode: 'history', // 使用HTML5历史记录模式，去除URL中的#
     routes: [
       { path: '/', component: HomePage },
       { path: '/about-us', component: AboutUsPage }
     ]
   })
   ```
5. **主入口文件**
   修改 `src/main.js`，引入并使用router：

   ```javascript
   import Vue from 'vue'
   import App from './App.vue'
   import router from './router'

   new Vue({
     router,
     render: h => h(App)
   }).$mount('#app')
   ```
6. **修改App组件**
   创建 `src/App.vue`，并在其中使用router-view来渲染当前路由对应的组件：

   ```html
   <template>
     <div id="app">
       <header>
         <!-- 可以添加导航栏 -->
         <nav>
           <router-link to="/">首页</router-link> |
           <router-link to="/about-us">关于我们</router-link>
         </nav>
       </header>
       <main>
         <router-view></router-view>
       </main>
     </div>
   </template>
   ```
7. **添加样式**
   可以在 `src/assets/css/main.css`中添加一些基本样式。例如，定义一个导航栏的基本样式：

   ```css
   /* src/assets/css/main.css */
   nav {
     background-color: #333;
     color: white;
     padding: 10px 0;
     text-align: center;
   }

   router-link {
     color: white;
     margin-right: 20px;
     text-decoration: none;
   }
   ```
8. **运行项目**
   在终端中启动开发服务器：

   ```bash
   npm run serve
   ```
9. **部署到生产环境**
   使用Vue CLI的命令将项目构建为生产版本并部署到服务器上。

现在，你已经成功创建了一个基本的VUE脚手架，使用了Vue和vue-router进行页面导航。你可以根据实际需求进一步扩展路由配置、组件内容以及样式设计。
