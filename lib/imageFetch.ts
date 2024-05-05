export const imageFetch = async (selectedImage: File | null, link: string) => {
    try {
        if (!selectedImage) {
            throw new Error("No selected image provided");
        }

        const formData = new FormData();
        formData.append('file', selectedImage);

        const response = await fetch(link, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Failed to fetch image: ${response.statusText}`);
        }

        return response;
    } catch (error) {
        console.error("Error fetching image:", error);
        return null;
    }
};
