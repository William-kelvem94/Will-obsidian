---
title: "Next.js Cheat Sheet"
description: "Quick reference for Next.js 14+ App Router"
tags: [cheatsheet, nextjs, react, frontend, typescript, jarvis-engenharia]
updated: 2026-06-05
date: 2026-04-27
---

# Next.js Cheat Sheet

Quick reference for Next.js 14+ (App Router).

---

## 🚀 Project Setup

```bash
# Create new project
npx create-next-app@latest my-app

# Options
# ✔ TypeScript? Yes
# ✔ ESLint? Yes
# ✔ Tailwind CSS? Yes
# ✔ `src/` directory? Yes
# ✔ App Router? Yes
# ✔ Import alias? @/*

# Run dev server
cd my-app
npm run dev
```

---

## 📁 File Structure (App Router)

```
app/
├── layout.tsx         # Root layout
├── page.tsx           # Home page (/)
├── loading.tsx        # Loading UI
├── error.tsx          # Error UI
├── not-found.tsx      # 404 page
├── about/
│   └── page.tsx       # /about
├── blog/
│   ├── page.tsx       # /blog
│   └── [slug]/
│       └── page.tsx   # /blog/my-post
└── api/
    └── users/
        └── route.ts   # /api/users
```

---

## 📄 Pages & Routing

### Basic Page

```tsx
// app/page.tsx
export default function Home() {
  return (
    <main>
      <h1>Hello Next.js</h1>
    </main>
  )
}
```

### Dynamic Routes

```tsx
// app/blog/[slug]/page.tsx
export default function BlogPost({ params }: { params: { slug: string } }) {
  return <h1>Post: {params.slug}</h1>
}

// app/shop/[category]/[id]/page.tsx
export default function Product({
  params
}: {
  params: { category: string; id: string }
}) {
  return <div>{params.category} - {params.id}</div>
}
```

### Catch-all Routes

```tsx
// app/docs/[...slug]/page.tsx
export default function Docs({ params }: { params: { slug: string[] } }) {
  // /docs/a/b/c → params.slug = ['a', 'b', 'c']
  return <div>{params.slug.join('/')}</div>
}
```

---

## 🎨 Layouts

### Root Layout (Required)

```tsx
// app/layout.tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <nav>Nav bar</nav>
        {children}
        <footer>Footer</footer>
      </body>
    </html>
  )
}
```

### Nested Layout

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="dashboard">
      <aside>Sidebar</aside>
      <main>{children}</main>
    </div>
  )
}
```

---

## 🔄 Data Fetching

### Server Component (Default)

```tsx
// app/posts/page.tsx
async function getPosts() {
  const res = await fetch('https://api.example.com/posts', {
    cache: 'no-store' // Force dynamic (no cache)
    // Or:
    // next: { revalidate: 60 } // ISR (revalidate every 60s)
  })
  return res.json()
}

export default async function Posts() {
  const posts = await getPosts()
  
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

### Client Component

```tsx
'use client'

import { useState, useEffect } from 'react'

export default function Posts() {
  const [posts, setPosts] = useState([])
  
  useEffect(() => {
    fetch('/api/posts')
      .then(res => res.json())
      .then(setPosts)
  }, [])
  
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

### Static Generation with Params

```tsx
// app/blog/[slug]/page.tsx

// Generate static pages at build time
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts').then(res => res.json())
  
  return posts.map((post) => ({
    slug: post.slug,
  }))
}

export default async function Post({ params }: { params: { slug: string } }) {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`)
    .then(res => res.json())
  
  return <article>{post.content}</article>
}
```

---

## 🌐 API Routes

### GET Request

```tsx
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
  ]
  
  return NextResponse.json(users)
}
```

### POST Request

```tsx
// app/api/users/route.ts
export async function POST(request: NextRequest) {
  const body = await request.json()
  
  // Save to database
  const user = { id: 3, ...body }
  
  return NextResponse.json(user, { status: 201 })
}
```

### Dynamic API Routes

```tsx
// app/api/users/[id]/route.ts
export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  const user = await fetchUser(params.id)
  
  if (!user) {
    return NextResponse.json({ error: 'Not found' }, { status: 404 })
  }
  
  return NextResponse.json(user)
}
```

---

## 🔐 Metadata & SEO

```tsx
// app/page.tsx
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'My Page',
  description: 'Page description',
  openGraph: {
    title: 'My Page',
    description: 'Page description',
    images: ['/og-image.png'],
  },
}

export default function Page() {
  return <div>Content</div>
}
```

### Dynamic Metadata

```tsx
// app/blog/[slug]/page.tsx
export async function generateMetadata({
  params
}: {
  params: { slug: string }
}): Promise<Metadata> {
  const post = await fetchPost(params.slug)
  
  return {
    title: post.title,
    description: post.excerpt,
  }
}
```

---

## 🎯 Navigation

### Link Component

```tsx
import Link from 'next/link'

export default function Nav() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href={`/blog/${slug}`}>Post</Link>
    </nav>
  )
}
```

### useRouter (Client)

```tsx
'use client'

import { useRouter } from 'next/navigation'

export default function Button() {
  const router = useRouter()
  
  return (
    <button onClick={() => router.push('/dashboard')}>
      Go to Dashboard
    </button>
  )
}
```

### Programmatic Navigation

```tsx
'use client'

import { useRouter } from 'next/navigation'

export default function LoginForm() {
  const router = useRouter()
  
  const handleSubmit = async (e) => {
    e.preventDefault()
    // Login logic
    router.push('/dashboard')
    router.refresh() // Refresh current route
  }
  
  return <form onSubmit={handleSubmit}>...</form>
}
```

---

## 🖼️ Images

```tsx
import Image from 'next/image'

export default function Avatar() {
  return (
    <Image
      src="/avatar.png"
      alt="Avatar"
      width={200}
      height={200}
      priority // Load immediately (above fold)
    />
  )
}

// External images (need domains in next.config.js)
<Image
  src="https://example.com/image.png"
  alt="External"
  width={200}
  height={200}
/>
```

### next.config.js

```js
module.exports = {
  images: {
    domains: ['example.com', 'cdn.example.com'],
  },
}
```

---

## 🛠️ Environment Variables

```bash
# .env.local
DATABASE_URL=postgresql://...
NEXT_PUBLIC_API_URL=https://api.example.com
```

```tsx
// Server-side
const dbUrl = process.env.DATABASE_URL

// Client-side (must start with NEXT_PUBLIC_)
const apiUrl = process.env.NEXT_PUBLIC_API_URL
```

---

## 🔄 Loading States

```tsx
// app/dashboard/loading.tsx
export default function Loading() {
  return <div>Loading...</div>
}
```

### Suspense

```tsx
import { Suspense } from 'react'

export default function Page() {
  return (
    <Suspense fallback={<div>Loading posts...</div>}>
      <Posts />
    </Suspense>
  )
}
```

---

## ⚠️ Error Handling

```tsx
// app/error.tsx
'use client'

export default function Error({
  error,
  reset,
}: {
  error: Error
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  )
}
```

### not-found.tsx

```tsx
// app/not-found.tsx
export default function NotFound() {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
    </div>
  )
}

// Trigger in page
import { notFound } from 'next/navigation'

export default async function Page({ params }) {
  const post = await fetchPost(params.slug)
  
  if (!post) {
    notFound()
  }
  
  return <div>{post.title}</div>
}
```

---

## 🎨 Styling

### CSS Modules

```tsx
// app/page.module.css
.container {
  padding: 20px;
}

// app/page.tsx
import styles from './page.module.css'

export default function Page() {
  return <div className={styles.container}>Content</div>
}
```

### Tailwind CSS

```tsx
export default function Page() {
  return (
    <div className="p-4 bg-gray-100 rounded-lg">
      <h1 className="text-2xl font-bold">Title</h1>
    </div>
  )
}
```

---

## 🚀 Deployment (Vercel)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Production deploy
vercel --prod
```

### vercel.json

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "framework": "nextjs"
}
```

---

## 🐳 Docker

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  nextjs:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
```

---

## 📦 Key Commands

```bash
# Dev
npm run dev

# Build
npm run build

# Start prod server
npm start

# Lint
npm run lint

# Type check
npx tsc --noEmit
```

---

## 🔗 Related

- [Next.js Docs](https://nextjs.org/docs)
- [[JARVIS/04-Engineering/Playbooks/Port-Already-In-Use|Port Troubleshooting]]
- [[skills/02-software-engineering|Software Engineering Skills]]

[[JARVIS/README|← Voltar ao Command Center]]
