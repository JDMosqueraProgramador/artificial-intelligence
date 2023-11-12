import { IProduct } from "./product";

export interface ICategory {
    id: number;
    categoryName: string;
    products: IProduct[];
}