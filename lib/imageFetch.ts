export const imageFetch = async (selectedImage: File | null, link: string) => {
    if (selectedImage) {
        const formData = new FormData();
        formData.append('file', selectedImage);

        const response = await fetch(link, {
            method: 'POST',
            body: formData
        });
        return response
    }
    return null;
};