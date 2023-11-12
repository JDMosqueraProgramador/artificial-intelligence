import { ICategory } from "./category";
import { ISupplier } from "./supplier";

export interface IProduct {
    id: number;
    productName: string;
    description: string;
    category: ICategory;
    categoryId: number;
    price: number;
    quantityInStock: number;
    supplier: ISupplier;
    supplierId: number;
    QR: string;
}