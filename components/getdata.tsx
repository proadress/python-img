"use client"

import { Button } from "./ui/button"

export const GetData = ()=>{
    return (
        <>
        <Button onClick={async()=>{
            const res = await fetch("/api/db/sensorData");
            const json = await res.json();
            console.log(json);

        }}></Button>
        </>
    )
}