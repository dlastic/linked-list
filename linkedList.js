class Node {
  constructor(value) {
    this.value = value;
    this.nextNode = null;
  }
}

export default class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  append(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    this.tail.nextNode = newNode;
    this.tail = newNode;
  }

  prepend(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    newNode.nextNode = this.head;
    this.head = newNode;
  }

  size() {
    let count = 0;
    let currentNode = this.head;
    while (currentNode) {
      count++;
      currentNode = currentNode.nextNode;
    }
    return count;
  }

  at(index) {
    if (index < 0) {
      console.log("Index out of bound");
      return null;
    }
    let currentIndex = 0;
    let currentNode = this.head;
    while (currentNode) {
      if (currentIndex === index) return currentNode;
      currentNode = currentNode.nextNode;
      currentIndex++;
    }
    console.log("Index out of bound");
    return null;
  }

  insertAt(value, index) {
    const listSize = this.size();

    if (index < 0 || index > listSize) {
      console.log("Index out of bound");
      return null;
    }

    if (index === 0) {
      this.prepend(value);
      return;
    }

    if (index === listSize) {
      this.append(value);
      return;
    }

    const newNode = new Node(value);
    const previousNode = this.at(index - 1);
    newNode.nextNode = previousNode.nextNode;
    previousNode.nextNode = newNode;
  }

  removeAt(index) {
    const listSize = this.size();

    if (index < 0 || index >= listSize) {
      console.log("Index out of bound");
      return null;
    }

    if (index === 0) {
      const currentNode = this.head;
      this.head = currentNode.nextNode;
      if (this.head === null) this.tail = null;
      currentNode.nextNode = null;
      return;
    }

    const previousNode = this.at(index - 1);
    const currentNode = previousNode.nextNode;
    previousNode.nextNode = currentNode.nextNode;

    if (currentNode === this.tail) {
      this.tail = previousNode;
    }

    currentNode.nextNode = null;
  }

  pop() {
    if (!this.head) return;
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
      return;
    }

    let currentNode = this.head;
    while (currentNode.nextNode !== this.tail) {
      currentNode = currentNode.nextNode;
    }

    currentNode.nextNode = null;
    this.tail = currentNode;
  }

  contains(value) {
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.value === value) return true;
      currentNode = currentNode.nextNode;
    }
    return false;
  }

  find(value) {
    let index = 0;
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.value === value) return index;
      currentNode = currentNode.nextNode;
      index++;
    }
    return null;
  }

  toString() {
    let nodeValueStrings = [];
    let currentNode = this.head;
    while (currentNode) {
      nodeValueStrings.push(`( ${String(currentNode.value)} )`);
      currentNode = currentNode.nextNode;
    }
    nodeValueStrings.push("null");

    return nodeValueStrings.join(" -> ");
  }
}
