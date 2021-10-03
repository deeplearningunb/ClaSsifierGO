import styled from 'styled-components';

export const Input = styled.input`
  margin: 24px 0;
`;

export const Image = styled.img`
  display: ${(props) => `${props.display}`};
`;

export const Button = styled.button`
  background-color: rgb(117,136,236);
  height: 32px;
  border: none;
  cursor: pointer;
`;

export const Page = styled.div`
`;

export const InputDiv = styled.div`
  width: min-content;
  border: 18px solid rgb(117,136,236);
  margin: 0 auto;
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
  font-size: 26px;
  margin-top: 0;
`;