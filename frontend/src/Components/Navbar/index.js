import React, { Component } from 'react';
import {
  Nav, Logo
} from './Style';

class Navbar extends Component {
  render() {
    return (
      <Nav>
        <Logo href="/">SudokuSolver</Logo>
      </Nav>
    );
  }
};

export default Navbar;