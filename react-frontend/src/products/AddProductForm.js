import React, { useState } from 'react';

const AddProductForm = () => {
  const [productName, setProductName] = useState('');
  const [category, setCategory] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    const productData = {
      productName,
      category,
    };

    fetch('http://localhost:5000/api/products/add', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(productData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Response:', data);
        // Handle the response from the server as needed
        setProductName("")
        setCategory("")
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle errors here
      });
  };

  return (
    <div>
        <form onSubmit={handleSubmit}>
            <div>
                <label>
                Product Name:
                <input
                    type="text"
                    value={productName}
                    onChange={(event) => setProductName(event.target.value)}
                />
                </label>
            </div>
            <div>
                <label>
                Category:
                <input
                    type="text"
                    value={category}
                    onChange={(event) => setCategory(event.target.value)}
                />
                </label>
            </div>
            <div>
                <button type="submit">Add Product</button>
            </div>
        </form>
    </div>
  );
};

export default AddProductForm;
