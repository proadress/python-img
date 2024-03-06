'use client'


import { ChangeEvent, useState } from "react";

export const DataImage: React.FC<{ link: string }> = ({ link }) => {

    const [imageUrl, setImageUrl] = useState(link);

    const reloadImage = () => {
        // 在图像URL后面加上一个随机参数来强制刷新图像
        setImageUrl(`${link}?${Math.random()}`);
    };

    return (
        <div>
            <img src={imageUrl} alt="Backend Image" />
            <button onClick={reloadImage}>Reload Image</button>
        </div>
    );
};



export const ImageUploader: React.FC = () => {
    const [selectedImage, setSelectedImage] = useState<File | null>(null);
    const [oriImage, setOriImage] = useState<string | null>(null);
    const [resImage, setResImage] = useState<string | null>(null);

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

    const handleUpload = async () => {
        if (selectedImage) {
            const formData = new FormData();
            formData.append('file', selectedImage);

            const response = await fetch('/api/image/res', {
                method: 'POST',
                body: formData
            });

            const blob = await response.blob();
            const imageUrl = URL.createObjectURL(blob);
            setResImage(imageUrl);
        }
    };

    return (
        <div>
            <input className="file-input file-input-bordered file-input-primary w-full max-w-xs" type="file" accept="image/*" onChange={handleImageChange} />
            {oriImage && <img className="h-72" src={oriImage} alt="Original Image" />}
            <button className="btn btn-primary" onClick={handleUpload}>Upload and Process</button>
            {resImage && <img className="h-72" src={resImage} alt="Modified Image" />}
        </div>
    );
};


