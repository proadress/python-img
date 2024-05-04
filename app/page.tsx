import { Menu } from "./menu";

const Home = async () => {
  return (
    <div>
      <div className='flex justify-center items-center h-screen space-x-4'>
        <Menu />
      </div>
    </div>
  );
};


export default Home;