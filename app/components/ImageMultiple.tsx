'use client'


import Image from "next/image";
import { ChangeEvent, useState } from "react";


const ImageUploader: React.FC = () => {
    const [selectedImages, setSelectedImages] = useState<File[]>([]);
    const [oriImages, setOriImages] = useState<string[]>([]);
    const [resImages, setResImages] = useState<number[][][]>([]);

    const handleImageChange = (event: ChangeEvent<HTMLInputElement>) => {
        const files = event.target.files;
        if (files) {
            const fileArray = Array.from(files);
            setSelectedImages(fileArray);

            const readerArray: FileReader[] = [];
            const oriImagesArray: string[] = [];

            fileArray.forEach((file) => {
                const reader = new FileReader();
                reader.onload = (e) => {
                    if (e.target?.result) {
                        oriImagesArray.push(e.target.result as string);
                        if (oriImagesArray.length === fileArray.length) {
                            setOriImages(oriImagesArray);
                        }
                    }
                };
                reader.readAsDataURL(file);
                readerArray.push(reader);
            });
        }
    };

    const handleUpload = async () => {
        if (selectedImages.length > 0) {
            const formData = new FormData();
            selectedImages.forEach((image) => {
                formData.append('files', image);
            });

            const response = await fetch('/api/image/mul', {
                method: 'POST',
                body: formData
            });
            const result = await response.json(); // Assuming the response is JSON
            const parsedData: number[][][] = JSON.parse(result);
            console.log(result);
            setResImages(parsedData); // Assuming 'images' is the key for the list of image URLs
        }
    };

    return (
        <div>
            <input className="file-input file-input-bordered file-input-primary w-full max-w-xs" type="file" accept="image/*" multiple onChange={handleImageChange} />
            <button className="btn btn-primary" onClick={handleUpload}>Upload and Process</button>
            {resImages.length > 0 && (
                <div>
                    {resImages.map((coordinates, index) => (
                        <div key={index}>
                            <ul >picture{index + 1}:{coordinates.map((point, idx) => ("[" + point.toString() + "]"))}</ul>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};


export default ImageUploader;