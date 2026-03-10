import { defineConfig } from 'vitepress'
import fs from 'fs'
import path from 'path'

// Helper to get all reports with advanced sorting
const getReports = () => {
  const reportsDir = path.resolve(__dirname, '../reports')
  if (!fs.existsSync(reportsDir)) return []
  return fs.readdirSync(reportsDir)
    .filter(file => file.endsWith('.md') && file !== 'index.md')
    .map(file => ({
      text: file.replace('.md', ''),
      link: `/reports/${file.replace('.md', '')}`,
      name: file.replace('.md', '')
    }))
    .sort((a, b) => {
      // Comparison logic: 
      // 1. Date (YYYY-MM-DD) descending
      // 2. Evening always above Morning for the same date
      if (a.name < b.name) return 1
      if (a.name > b.name) return -1
      return 0
    })
    // Note: Since 'evening' starts with 'e' and 'morning' with 'm', 
    // alphabetical DESC ('m' to 'a') would put morning first.
    // However, filenames are YYYY-MM-DD-evening/morning.
    // '2026-03-09-morning' vs '2026-03-09-evening': 
    // 'm' > 'e'. In DESC sort, 'morning' comes first.
    // We actually need a custom rule: if date is same, 'evening' > 'morning'.
    .sort((a, b) => {
       const dateA = a.name.substring(0, 10);
       const dateB = b.name.substring(0, 10);
       if (dateA !== dateB) return dateB.localeCompare(dateA);
       // Same date: force 'evening' to be "smaller" in index (top)
       return a.name.includes('evening') ? -1 : 1;
    })
}

export default defineConfig({
  base: '/finance-auto-gen/',
  title: "全天候金融洞察",
  description: "AI 驱动的全球市场早晚报",
  head: [
    ['link', { rel: 'icon', href: '/finance-auto-gen/favicon.png' }]
  ],
  themeConfig: {
    search: {
      provider: 'local'
    },
    nav: [
      { text: '首页', link: '/' },
      { text: '市场简报', link: '/reports/' }
    ],
    sidebar: {
      '/reports/': [
        {
          text: '历史简报',
          items: getReports()
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
