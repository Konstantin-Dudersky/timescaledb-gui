"""Модели данных."""

from pydantic import BaseModel, Field


class Hypertable(BaseModel):
    """Metadata information about hypertables."""

    hypertable_schema: str = Field(description="Schema name of the hypertable")
    hypertable_name: str = Field(description="Table name of the hypertable")
    owner: str = Field(description="Owner of the hypertable")
    num_dimensions: int = Field(description="Number of dimensions")
    num_chunks: int = Field(description="Number of chunks")
    compression_enabled: bool = Field(
        description="Is compression enabled on the hypertable?",
    )
    is_distributed: bool = Field(description="Is the hypertable distributed?")
    replication_factor: int | None = Field(
        description="Replication factor for a distributed hypertable",
    )
    data_nodes: str | None = Field(
        description="Nodes on which hypertable is distributed",
    )
    tablespaces: str | None = Field(
        description="Tablespaces attached to the hypertable",
    )
