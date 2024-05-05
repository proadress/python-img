import { ImageUploader } from "@/app/car/single/Image";

const Home = async () => {
    // const test = await (await fetch("/api/test")).json();
    return (
        <div>
            <div className='flex justify-center'>
                <ImageUploader link="/api/car/image/res" />
            </div>
        </div>
    );
};


export default Home;