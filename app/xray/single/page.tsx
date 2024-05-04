import { ImageUploader } from '@/app/xray/single/Image';

const Home = async () => {
  return (
    <div>
      <div className='flex justify-center'>
        <ImageUploader link="/api/xray/image/res" />
      </div>
    </div>
  );
};


export default Home;