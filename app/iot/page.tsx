import { BusSit } from "@/components/getdata";

const Home = async () => {
    const temp = 14;
    const seats = [];
    for (let i = 0; i < temp; i++) {
        if (i % 4 === 2) {
            seats.push(<div key={`space-${i}`} className="w-12 h-12"></div>);
        }
        if (i === 1) {
            seats.push(<BusSit key={i} sitid={i} />);
        } else {
            seats.push(<div className={"w-12 h-12 border-2 border-black"} />)
        }
    }
    return (
        <div>
            <div className='flex justify-center items-center h-screen space-x-4'>
                {/* <Menu /> */}
                <div className=" h-screen flex justify-center items-center">
                    <div className="bg-white p-6 rounded-lg shadow-md w-full max-w-md space-y-4">
                        <h1 className="text-2xl font-bold mb-4">bus</h1>
                        <div className="grid grid-cols-2 border-2 border-black rounded-md p-2">
                            <div>
                                <div className={"w-6 h-6 border-2 border-black"} />
                                <div>not used</div>
                            </div>
                            <div>
                                <div className={"w-6 h-6 bg-red-500"} />
                                <div> used</div>
                            </div>
                        </div>
                        <div className="grid grid-cols-5 gap-4">
                            {seats}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};


export default Home;