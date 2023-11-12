import { IProduct } from "./product";

export interface ISupplier {
    id: number;
    supplierName: string;
    contactName: string;
    email: string;
    phone: string;
    products?: IProduct[];
}