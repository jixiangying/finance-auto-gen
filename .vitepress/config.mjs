import { defineConfig } from 'vitepress'
import fs from 'fs'
import path from 'path'

// Helper to get all reports
const getReports = () => {
  const reportsDir = path.resolve(__dirname, '../reports')
  if (!fs.existsSync(reportsDir)) return []
  return fs.readdirSync(reportsDir)
    .filter(file => file.endsWith('.md'))
    .map(file => ({
      text: file.replace('.md', ''),
      link: `/reports/${file.replace('.md', '')}`
    }))
    .reverse() // Newest first
}

export default defineConfig({
  title: "全天候金融洞察",
  description: "AI 驱动的全球市场早晚报",
  themeConfig: {
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
