import { defineConfig } from 'vitepress'
import fs from 'fs'
import path from 'path'

// Helper to get week range (Monday to Sunday) and a sortable timestamp
const getWeekInfo = (dateStr) => {
  const [year, month, day] = dateStr.split('-').map(Number)
  const date = new Date(year, month - 1, day)
  const dayOfWeek = date.getDay() || 7 // 1 (Mon) to 7 (Sun)
  
  const monday = new Date(date)
  monday.setDate(date.getDate() - dayOfWeek + 1)
  
  const sunday = new Date(monday)
  sunday.setDate(monday.getDate() + 6)
  
  const format = (d) => `${d.getMonth() + 1}.${d.getDate()}`
  return {
    range: `${format(monday)} - ${format(sunday)}`,
    mondayTime: monday.getTime()
  }
}

// Helper to get all reports grouped by Year and Week Range
const getGroupedReports = () => {
  const reportsDir = path.resolve(__dirname, '../reports')
  if (!fs.existsSync(reportsDir)) return []
  
  const files = fs.readdirSync(reportsDir)
    .filter(file => file.endsWith('.md') && file !== 'index.md')
    .map(file => {
      const name = file.replace('.md', '')
      const dateStr = name.substring(0, 10)
      const { range, mondayTime } = getWeekInfo(dateStr)
      return {
        text: name.includes('morning') ? `${dateStr} 上午` : (name.includes('evening') ? `${dateStr} 下午` : name),
        link: `/reports/${name}`,
        name: name,
        year: dateStr.substring(0, 4),
        weekRange: range,
        mondayTime: mondayTime
      }
    })
    .sort((a, b) => {
      if (a.name.substring(0, 10) !== b.name.substring(0, 10)) {
        return b.name.localeCompare(a.name)
      }
      return a.name.includes('evening') ? -1 : 1
    })

  const groups = []
  const yearMap = new Map()

  files.forEach(report => {
    if (!yearMap.has(report.year)) {
      const yearGroup = {
        text: `${report.year}年`,
        collapsed: false,
        items: []
      }
      yearMap.set(report.year, yearGroup)
      groups.push(yearGroup)
    }

    const yearGroup = yearMap.get(report.year)
    let weekGroup = yearGroup.items.find(i => i.text === report.weekRange)
    
    if (!weekGroup) {
      weekGroup = {
        text: report.weekRange,
        mondayTime: report.mondayTime,
        collapsed: true,
        items: []
      }
      yearGroup.items.push(weekGroup)
    }
    
    weekGroup.items.push({
      text: report.text,
      link: report.link
    })
  })

  // Sort weeks within years (descending by Monday's timestamp)
  groups.forEach(yearGroup => {
    yearGroup.items.sort((a, b) => b.mondayTime - a.mondayTime)
  })

  return groups
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
      '/reports/': getGroupedReports()
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
