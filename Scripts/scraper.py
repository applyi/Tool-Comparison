
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Scraper(ABC):

    @abstractmethod
    def scrape(self) -> List[str]:
        ...
