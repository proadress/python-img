import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { ImageUploader } from '../components/Image';

const Home = async () => {
  return (
    <div>
      <div className='flex justify-center'>
        <ImageUploader />
      </div>
    </div>
  );
};


export default Home;