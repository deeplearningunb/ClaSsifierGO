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
`;

export const Page = styled.div`
`;

export const InputDiv = styled.div`
  background-color: #ffffff;
  box-shadow: 10px 10px 20px grey;
  width: min-content;
  border: 10px solid #ffffff;
  margin: 20px auto;
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
  font-size: 32px;
  margin-top: 0;
`;
