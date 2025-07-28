import LinkedList from "./linkedList.js";

const list = new LinkedList();

list.append("dog");
list.append("cat");
list.append("parrot");
list.append("hamster");
list.append("snake");
list.append("turtle");

console.log(list.toString());

list.insertAt("INSERTED NODE", 5);
console.log(list.toString());

list.removeAt(0);
console.log(list.toString());
