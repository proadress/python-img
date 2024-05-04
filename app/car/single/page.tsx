import { ImageUploader } from "@/app/car/single/Image";

const Home = async () => {
    return (
        <div>
            <div className='flex justify-center'>
                <ImageUploader link="/api/car/image/res" />
            </div>
        </div>
    );
};


export default Home;