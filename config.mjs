
/**
 * @type {import("../config/siteConfig").UserConfig}
 */
const config = {
    title: "SunshineNotes",
    description: "Record the difficulties and steps encountered in self-learning technology",
    author: "Sunshine AI",
    logo: "/images/icons/logo.png",
    domain: "https://github.com/SunshineAI0523",
    navbarTitle: {
      logo: "/images/icons/logo.png",
      text: "朝阳笔记SunshineNotes",
      version: "Stable"
    },
    editLinkRoot:
      "https://github.com/SunshineAI0523/SunshineNotes/edit/main",
    showEditLink: true,
    showToc: true,
    showSidebar: true,
    showComments: false,
    comments: {
      provider: "giscus", // supported providers: giscus, utterances, disqus
      pages: ["blog"], // page directories where we want commments
      config: {
        repo: process.env.NEXT_PUBLIC_GISCUS_REPO,
        repositoryId: process.env.NEXT_PUBLIC_GISCUS_REPOSITORY_ID,
        category: process.env.NEXT_PUBLIC_GISCUS_CATEGORY,
        categoryId: process.env.NEXT_PUBLIC_GISCUS_CATEGORY_ID,
      },
    },
    analytics: "",
    navLinks: [
      // { href: "/", name: "主页" },
      // { href: "/各种折腾", name: "各种折腾" },
      // { href: "/编程相关", name: "编程相关" },
      // { href: "/朝阳笔记", name: "朝阳笔记" },
      // { href: "/旅行日记", name: "旅行日记" },
      // { href: "/本站简介/", name: "本站简介" },
      // { href: "/_all", name: "所有标签" },
    ],
    social: [
      { label: "github", href: "https://github.com/SunshineAI0523" },
    ],
    search: {
      provider: "algolia",
      config: {
        appId: process.env.NEXT_PUBLIC_DOCSEARCH_APP_ID,
        apiKey: process.env.NEXT_PUBLIC_DOCSEARCH_API_KEY,
        indexName: process.env.NEXT_PUBLIC_DOCSEARCH_INDEX_NAME,
      },
    },
    nextSeo: {
      titleTemplate: "%s | SunshineAI",
      description:
        "Record the difficulties and steps encountered in self-learning technology",
      canonical: "https://github.com/SunshineAI0523",
      // openGraph: {
      //   title: "SunshineNotes",
      //   images: [
      //     {
      //       url: "https://SunshineNotes.app/assets/images/frontpage-screenshot.jpg",
      //       alt: "SunshineNotes",
      //       width: 1200,
      //       height: 627,
      //       type: "image/jpg",
      //     },
      //   ],
      // },
      // twitter: {
      //   handle: "@SunshineNotes",
      //   site: "https://SunshineNotes.app",
      //   cardType: "summary_large_image",
      // },
    },
  };
  
export default config;


