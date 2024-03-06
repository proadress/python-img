
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

// export const metadata: Metadata = {
//   title: '視知覺科技IoT雲端Line通知',
//   description: '視知覺科技',
// }

export default function RootLayout({ children, }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="h-full">
      <body>
        <main className="relative flex flex-col min-h-screen">
          <div className="flex-grow flex-1">{children}</div>
        </main>
      </body>
    </html>
  )
}
