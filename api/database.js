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

    // Query the quotes table, joining with the authors table to get author names
    const quotes = await db.all(`
      SELECT quotes.quote_id, quotes.quote, authors.author_name
      FROM quotes
      JOIN authors ON quotes.author_id = authors.author_id
    `);

    // Close the database
    await db.close();

    // Return the data as a JSON response
    res.status(200).json({ quotes, authors });
  } catch (err) {
    console.error('Database error:', err);
    res.status(500).json({ error: 'Failed to fetch data from the database' });
  }
}
