"use client"

import { useEffect, useState } from "react";
import { Button } from "./ui/button"

export const BusSit = ({ sitid }: { sitid: number }) => {
    const [seatStatus, setSeatStatus] = useState(false);

    useEffect(() => {
        fetchAllSeatStatus();
        const interval = setInterval(() => {
            fetchAllSeatStatus();
        }, 2000); // 每隔5秒重新加载数据

        return () => clearInterval(interval); // 清除定时器
    }, []);

    const fetchAllSeatStatus = async () => {
        const res = await fetch("http://localhost:3000/api/db/sensorData/" + sitid);
        if (!res.ok) {
            return <div className="w-12 h-12 border-2"></div>
        }
        setSeatStatus((await res.json())['dis'] < 40);
    }

    return (
        <div className={"w-12 h-12 border-2" + (seatStatus ? " border-black bg-red-500" : " border-black")
        } />
    );
}