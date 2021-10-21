import styled from 'styled-components';

export const Input = styled.input`
  margin: 24px 0;
`;

export const Image = styled.img`
  display: ${(props) => `${props.display}`};
  border-radius: 12px;
`;

export const Button = styled.button`
  background-color: rgb(192,192,192);
  height: 32px;
  border: none;
  cursor: pointer;
  border-radius:5px
`;

export const Page = styled.div`
`;

export const InputDiv = styled.div`
  background-color: #ffffff;
  box-shadow: 10px 10px 5px gray;
  width: min-content;
  border: 10px solid #ffffff;
  margin: 64px auto;
  display: flex;
  flex-direction: column;
  border-radius: 12px;
  padding: 36px;
`;

export const ImageDiv = styled.div`
`;

export const P = styled.p`
  text-align: center;
  letter-spacing: 3px;
  font-size: 42px;
  margin-top: 0;
`;
