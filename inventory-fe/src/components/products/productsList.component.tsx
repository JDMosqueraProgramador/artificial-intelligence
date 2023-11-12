import { IProduct } from "../../types/product";
import { Product } from "./product.component";

export interface ProductListProps {
    products: IProduct[];
}

export const ProductList = ({ products }: ProductListProps) => {
    return (
        <div className="bg-gray-100 min-h-screen flex items-center justify-center">
            {
                products.map(
                    (product) => <Product {...product} key={product.id} />
                )
            }
        </div>
    )
}