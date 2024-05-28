// import { GetData } from "@/components/getdata";
import { Menu } from "./menu";
import { redirect } from "next/navigation";

const Home = async () => {
  redirect("iot");
  return (
    <div>
      <div className='flex justify-center items-center h-screen space-x-4'>
        <Menu />
        {/* <GetData /> */}
      </div>
    </div>
  );
};


export default Home;