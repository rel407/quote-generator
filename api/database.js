import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

// This is your serverless function
export default async function handler(req, res) {
  try {
    // Open the SQLite database
    const db = await open({
      filename: './quotes-proj.db', // Ensure this path is correct
      driver: sqlite3.Database
    });

    // Example query: Fetching all rows from two tables (quotes and authors)
    // Replace 'quotes' and 'authors' with your actual table names
    const quotes = await db.all('SELECT * FROM quotes');
    const authors = await db.all('SELECT * FROM authors');

    // Close the database
    await db.close();

    // Return the data as a JSON response
    res.status(200).json({ quotes, authors });
  } catch (err) {
    console.error('Database error:', err);
    res.status(500).json({ error: 'Failed to fetch data from the database' });
  }
}
