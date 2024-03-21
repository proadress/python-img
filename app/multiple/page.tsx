import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { ImageUploader } from '../components/Image';
import ImageMultiple from '../components/ImageMultiple';

const Home = async () => {
  return (
    <div>
      <div className='flex justify-center'>
        <ImageMultiple />
      </div>
    </div>
  );
};


export default Home;