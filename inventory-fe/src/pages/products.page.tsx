import { useEffect, useState } from "react";
import { ProductList } from "../components/products/productsList.component";
import axios from "axios";
import { IProduct } from "../types/product";
import { BE_URL } from "../config/costants";

export const ProductsPage = () => {
    const [products, setProducts] = useState<IProduct[]>([]);

    const getProducts = async () => {
        try {
            const response = await axios.get<IProduct[]>(BE_URL);
            setProducts(response.data);
        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => {
        getProducts();
        setInterval(getProducts, 3000);
    }, []);

    return (
        <section>
            <h1 className="text-3xl font-bold my-2">List of products</h1>
            <ProductList products={products} />
        </section>
    );
}