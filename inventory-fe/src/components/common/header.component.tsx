import React from 'react';
import { Link, Outlet } from 'react-router-dom';

const Header = () => {
    return (
        <>
            <header className="bg-gray-800 text-white p-4">
                <nav>
                    <ul className="flex">
                        <li className="mr-6">
                            <Link to="/products" className="hover:text-gray-300">Products</Link>
                        </li>
                        <li className="mr-6">
                            <Link to="/categories" className="hover:text-gray-300">Categories</Link>
                        </li>
                        <li className="mr-6">
                            <Link to="/suppliers" className="hover:text-gray-300">Suppliers</Link>
                        </li>
                    </ul>
                </nav>
            </header>
            <Outlet />
        </>

    );
};

export default Header;