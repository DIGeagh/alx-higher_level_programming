#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Convert arguments to numbers
const uniqueArgs = [...new Set(args)]; // Remove duplicates

if (uniqueArgs.length < 2) {
  console.log(0);
} else {
  const sortedArgs = uniqueArgs.sort((a, b) => b - a); // Sort in descending order
  console.log(sortedArgs[1]); // Print the second largest
}
