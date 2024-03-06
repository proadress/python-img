import React, { useState, useEffect } from 'react';
import { DataImage, ImageUploader } from './components/Image';

const Home = async () => {
  return (
    <div>
      <div className=''>
        <ImageUploader />
      </div>
    </div>
  );
};


export default Home;