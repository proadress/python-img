import React, { useState, useEffect } from 'react';
import { DataImage, ImageUploader } from './components/Image';
import Link from 'next/link';

const Home = async () => {
  return (
    <div>
      <div className='flex justify-center items-center h-screen space-x-4'>
        <Link href="/single" className='btn btn-primary text-lg'>single</Link>
        <Link href="/multiple" className='btn btn-primary text-lg'>multiple</Link>

      </div>
    </div>
  );
};


export default Home;