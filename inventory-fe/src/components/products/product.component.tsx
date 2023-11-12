import { useEffect, useState } from "react";
import { IProduct } from "../../types/product";
const saveSvgAsPng = require('save-svg-as-png');


export const Product = ({ id, productName, description, category, QR ,quantityInStock, price }: IProduct) => {
    const [processedQR, setProcessedQR] = useState<string>('');

    useEffect(() => {
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        const [_, qrPart2] = QR.split('<svg', 2);
        setProcessedQR(`<svg id="${id}-qr" ${qrPart2}`);
    }, [QR, id]);

    const handleDownload = () => {
        saveSvgAsPng.saveSvgAsPng(document.getElementById(`${id}-qr`), `${id}-${productName}-qr.png` ,{
            scale: 10,
            encoderOptions: 1,
            backgroundColor: 'white',
        }); 
    }

    return (
        <div className="max-w-md bg-white rounded overflow-hidden shadow-lg my-10 mx-5 p-5">
            <div className="px-6 py-4">
                <div className="font-bold text-xl mb-2">{productName}</div>
                <p className="text-gray-700 text-base">{description}</p>
            </div>

            <div className="px-6 py-2">
                <span>Current stock: </span><span>{quantityInStock}</span>
            </div>

            <div className="px-6 py-4">
                <span
                    className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2"
                >
                    {category?.categoryName}
                </span>
            </div>

            <div className="px-6 py-4">
                <span className="text-xl font-semibold text-gray-900">${price}</span>
            </div>

            <div 
                dangerouslySetInnerHTML={{ __html: processedQR }}
            />

            <div className="px-6 py-4">
                <button 
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 w-full rounded-full"
                    onClick={() => handleDownload()}
                >
                    Download QR
                </button>
            </div>

        </div>
    )
}