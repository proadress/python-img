
import type { Metadata } from 'next'
import './globals.css'
import { ThemeProvider } from '@/components/theme-provider'


export const metadata: Metadata = {
  title: '豪華版python影像辨識平臺',
  description: 'fast api + next js',
}

export default function RootLayout({ children, }: { children: React.ReactNode }) {
  return (
    <html suppressHydrationWarning={true} lang="en">
      <body>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <main className="relative flex flex-col min-h-screen bg-slate-200 dark:bg-slate-600">
            <div className="flex-grow flex-1">{children}</div>
          </main>
        </ThemeProvider>
      </body>
    </html>
  )
}
