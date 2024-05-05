'use client'
import Image from "next/image";
import { ChangeEvent, useState } from "react";
import { Input } from "../../../components/ui/input";
import { Button } from "../../../components/ui/button";
import { imageFetch } from "@/lib/imageFetch";

export const ImageUploader: React.FC<{ link: string }> = ({ link }) => {
    const [selectedImage, setSelectedImage] = useState<File | null>(null);
    const [oriImage, setOriImage] = useState<string | null>(null);
    const [resImage, setResImage] = useState<string | null>(null);
    const [test, setTest] = useState<string | null>(null);

    const handleImageChange = (event: ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];
        if (file) {
            setSelectedImage(file);
            const reader = new FileReader();
            reader.onload = (e) => {
                setOriImage(e.target?.result as string);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleUpload = async (selectedImage: File | null) => {
        const response = await imageFetch(selectedImage, link);
        if (!response) { console.error("no response from"); return }
        console.log(123);

        console.log(response);

        setResImage(await response.json());
    }


    return (
        <div className=" bg-slate-400 p-8 rounded-lg space-y-4">
            <div className="grid w-full max-w-sm items-center gap-1.5">
                <Input type="file" accept="image/*" onChange={handleImageChange} />
            </div>
            {oriImage && <Image width={500} height={500} src={oriImage} alt="Original Image" />}
            <Button onClick={() => handleUpload(selectedImage)}>Upload and Process</Button>
            {resImage}
            <Button onClick={async () => {
                const test = await (await fetch("/api/test")).json()
                console.log(test);
                setTest(test);

            }}>get test</Button>
            <div>{test && test}</div>

        </div>
    );
};


