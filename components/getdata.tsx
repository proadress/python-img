'use client'
import { useEffect, useState } from "react";
import { Button } from "./ui/button";

export const BusSit = ({ sitid }: { sitid: number }) => {
    const [seatStatus, setSeatStatus] = useState(false);
    const COUNT = 3;
    const [countdown, setCountdown] = useState(COUNT); // Initial countdown value in seconds

    useEffect(() => {
        fetchAllSeatStatus();
        // const interval = setInterval(() => {
        //     fetchAllSeatStatus();
        // }, 5000); // Fetch data every 2 seconds

        const countdownInterval = setInterval(() => {
            setCountdown(prevCountdown => {
                if (prevCountdown === 0) {
                    fetchAllSeatStatus();
                    return COUNT; // Reset countdown when it reaches 1
                }
                return prevCountdown - 1;
            });
        }, 1000); // Update countdown every second

        return () => {
            // clearInterval(interval); // Clear fetch interval
            clearInterval(countdownInterval); // Clear countdown interval
        };
    }, []);

    const fetchAllSeatStatus = async () => {
        const res = await fetch("https://python-img.vercel.app/api/db/sensorData/" + sitid);
        if (!res.ok) {
            return;
        }
        setSeatStatus((await res.json())['dis'] < 40);
        // setCountdown(2); // Reset countdown when data is fetched
    };

    return (
        <div className="flex flex-col items-center">
            <div className={"w-12 h-12 border-2" + (seatStatus ? " border-black bg-red-500" : " border-black")}></div>
            <div>{countdown}秒</div>
        </div>
    );
};
