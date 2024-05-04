import { ImageUploader } from "@/components/ImageMultiple";

const Home = async () => {
  return (
    <div>
      <div className='flex justify-center'>
        <ImageUploader link="/api/xray/image/mul" />
      </div>
    </div>
  );
};


export default Home;