import styled from 'styled-components';

export const Input = styled.input`
  margin: 24px 0;
`;

export const Image = styled.img`
  display: ${(props) => `${props.display}`};
`;

export const Button = styled.button`
  background-color: Transparent;
  height: 28px;
  border: 1px solid black;
  cursor: pointer;
`;

export const Page = styled.div`
`;

export const InputDiv = styled.div`
  width: min-content;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  border: 1px solid black;
  padding: 36px;
`;

export const ImageDiv = styled.div`
`;