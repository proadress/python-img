import { GetData } from "@/components/getdata";
import { Menu } from "./menu";

const Home = async () => {
  return (
    <div>
      <div className='flex justify-center items-center h-screen space-x-4'>
        <Menu />
        <GetData/>
      </div>
    </div>
  );
};


export default Home;